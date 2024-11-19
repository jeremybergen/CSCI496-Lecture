import cv2
import numpy as np


def get_observation(frame):
    img_copy = frame.copy()
    img_copy = cv2.cvtColor(img_copy, cv2.COLOR_BGR2HSV)
    # print(img_copy[180, 460])
    # cv2.imshow('img', img_copy)
    # cv2.waitKey(0)
    color_low = np.array([7, 150, 100])
    color_high = np.array([15, 205, 255])
    mask = cv2.inRange(img_copy, color_low, color_high)
    # cv2.imshow('mask', mask)
    # cv2.waitKey(30)

    edges = cv2.Canny(mask, 100, 200)
    x, y, w, h = cv2.boundingRect(edges)
    cent_x = x+w//2
    cent_y = y+h//2
    measurements = np.array([[cent_x], [cent_y]], np.float32).flatten()
    return measurements


def predict_particles(particles, std_dev):
    noise = np.random.randn(len(particles), 2) * 5
    particles += noise
    return particles


def update_weights(particles, weights, observation, std_dev):
    distance = np.linalg.norm(particles - observation, axis=1)
    weights = np.exp(-distance**2 / (2*std_dev**2))
    weights /= np.sum(weights)
    return weights


def resample_particles(particles, weights, num_particles):
    indices = np.random.choice(range(num_particles), size=num_particles, p=weights)
    particles = particles[indices]
    weights = np.ones(num_particles)/ num_particles
    return particles, weights


def smooth_observation(observation, prev_observation, alpha=0.6):
    if prev_observation is None:
        return observation
    return alpha * observation + (1-alpha) * prev_observation


def main() -> None:
    cap = cv2.VideoCapture("output.mp4")
    ret, frame = cap.read()

    num_particles = 1000
    particle_std_dev = 40

    particles = np.random.rand(num_particles, 2) * np.array([frame.shape[1], frame.shape[0]])
    frame_copy = frame.copy()
    for particle in particles:
        cv2.circle(frame_copy, (int(particle[0]), int(particle[1])), 2, (0, 255, 0), -1)

    cv2.imshow('frame_copy', frame_copy)
    cv2.waitKey(0)

    weights = np.ones(num_particles)/num_particles

    observation = get_observation(frame)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        prev_observation = observation
        observation = get_observation(frame)
        observation = observation.reshape(1, 2)
        new_observation = smooth_observation(observation, prev_observation)

        particles = predict_particles(particles, particle_std_dev)

        weights = update_weights(particles, weights, new_observation, particle_std_dev)

        particles, weights = resample_particles(particles, weights, num_particles)

        for particle in particles:
            cv2.circle(frame, (int(particle[0]), int(particle[1])), 2, (0, 255, 0), -1)

        cv2.imshow('frame', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    main()