import numpy as np
import cv2

# Parameters
num_particles = 1000  # Number of particles
noise_std = 15  # Standard deviation for particle motion noise
tracking_std = 30  # Standard deviation for initializing particles around target

# Load a sequence of images (e.g., from a video file)
video = cv2.VideoCapture("output.mp4")  # Replace with your video file path

# Initial object position (set by initial (x, y) point)
initial_x, initial_y = 460, 170  # Replace with your starting point
target_position = np.array([initial_x, initial_y])

# Initialize particles around the initial position with Gaussian noise
particles = np.random.normal(target_position, tracking_std, (num_particles, 2))

# Capture the first frame to get the target color
ret, initial_frame = video.read()
if not ret:
    print("Failed to read video.")
    video.release()
    exit()

# Extract the target color at the initial point
target_color = initial_frame[initial_y, initial_x]  # Get color as a reference for tracking

# Function to update particles by applying random motion noise
def predict_particles(particles, noise_std):
    particles += np.random.normal(0, noise_std, particles.shape)
    return particles

# Function to measure weights based on color similarity to initial target color
def measure_weights(particles, frame, target_color, noise_std):
    weights = np.zeros(len(particles))

    for i, particle in enumerate(particles):
        x, y = int(particle[0]), int(particle[1])
        # Ensure particle is within frame boundaries
        if 0 <= x < frame.shape[1] and 0 <= y < frame.shape[0]:
            particle_color = frame[y, x]
            # Compute color distance and assign weights based on it
            distance = np.linalg.norm(target_color - particle_color)
            weights[i] = np.exp(-distance ** 2 / (2 * noise_std ** 2))

    weights += 1e-10  # Avoid division by zero
    weights /= weights.sum()  # Normalize weights
    return weights

# Function to resample particles based on weights
def resample_particles(particles, weights):
    indices = np.random.choice(len(particles), len(particles), p=weights)
    resampled_particles = particles[indices]
    return resampled_particles

# Function to estimate target position from particles
def estimate_position(particles):
    return np.mean(particles, axis=0)

# Tracking loop
while True:
    ret, frame = video.read()
    if not ret:
        break  # End of video

    # Predict particles with random movement and noise
    particles = predict_particles(particles, noise_std)

    # Measure weights based on color similarity to initial target color
    weights = measure_weights(particles, frame, target_color, noise_std)

    # Resample particles based on weights
    particles = resample_particles(particles, weights)

    # Estimate target position from particles
    estimated_position = estimate_position(particles)

    # Draw particles, initial target, and estimated position
    for particle in particles:
        cv2.circle(frame, tuple(particle.astype(int)), 2, (0, 0, 255), -1)  # Particles in red
    cv2.circle(frame, (initial_x, initial_y), 8, (255, 0, 0), -1)  # Initial target position in blue
    cv2.circle(frame, tuple(estimated_position.astype(int)), 6, (0, 255, 0), -1)  # Estimated position in green

    # Display the frame
    cv2.imshow("Particle Filter Tracking by Color", frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()


# import numpy as np
# import cv2
#
# # Parameters
# num_particles = 1000  # Number of particles
# frame_size = (500, 500)  # Assuming size of the frames if needed
# noise_std = 15  # Standard deviation for motion noise
# tracking_std = 30  # Gaussian standard deviation to simulate object region
#
# # Load a sequence of images (e.g., from a video file)
# video = cv2.VideoCapture("output.mp4")  # Replace with path to your video file
# # ret, frame = video.read()
# # cv2.imshow('frame', frame)
# # cv2.waitKey(0)
#
# # Initial object position (in a real scenario, you might initialize this based on user input)
# initial_x, initial_y = 460, 170  # Replace with your initial position
# target_position = np.array([initial_x, initial_y])
#
# # Initialize particles around the initial position with some noise
# particles = np.random.normal(target_position, tracking_std, (num_particles, 2))
#
# # Function to update particles with random movement and noise
# def predict_particles(particles, noise_std):
#     particles += np.random.normal(0, noise_std, particles.shape)
#     return particles
#
# # Function to measure weights based on color similarity in a region around target
# def measure_weights(particles, frame, target_position, noise_std):
#     weights = np.zeros(len(particles))
#     target_color = frame[int(target_position[1]), int(target_position[0])]  # Get target color
#
#     for i, particle in enumerate(particles):
#         x, y = int(particle[0]), int(particle[1])
#         # Ensure particle is within frame boundaries
#         if 0 <= x < frame.shape[1] and 0 <= y < frame.shape[0]:
#             particle_color = frame[y, x]
#             # Compute color distance and assign weights based on it
#             distance = np.linalg.norm(target_color - particle_color)
#             weights[i] = np.exp(-distance ** 2 / (2 * noise_std ** 2))
#
#     weights += 1e-10  # Avoid division by zero
#     weights /= weights.sum()  # Normalize weights
#     return weights
#
# # Function to resample particles based on weights
# def resample_particles(particles, weights):
#     indices = np.random.choice(len(particles), len(particles), p=weights)
#     resampled_particles = particles[indices]
#     return resampled_particles
#
# # Function to estimate target position from particles
# def estimate_position(particles):
#     return np.mean(particles, axis=0)
#
# # Tracking loop
# while True:
#     ret, frame = video.read()
#     if not ret:
#         break  # End of video
#
#     # Predict particles
#     particles = predict_particles(particles, noise_std)
#
#     # Measure weights based on color similarity around target
#     weights = measure_weights(particles, frame, target_position, noise_std)
#
#     # Resample particles based on weights
#     particles = resample_particles(particles, weights)
#
#     # Estimate target position from particles
#     estimated_position = estimate_position(particles)
#
#     # Draw particles, target, and estimated position
#     for particle in particles:
#         cv2.circle(frame, tuple(particle.astype(int)), 2, (0, 0, 255), -1)  # Particles in red
#     cv2.circle(frame, tuple(target_position.astype(int)), 8, (255, 0, 0), -1)  # Initial target position in blue
#     cv2.circle(frame, tuple(estimated_position.astype(int)), 6, (0, 255, 0), -1)  # Estimated position in green
#
#     # Display the frame
#     cv2.imshow("Particle Filter Tracking", frame)
#     if cv2.waitKey(30) & 0xFF == ord('q'):
#         break
#
# video.release()
# cv2.destroyAllWindows()
#
#
# # import numpy as np
# # import cv2
# # import matplotlib.pyplot as plt
# #
# # # Parameters
# # num_particles = 100  # Number of particles
# # frame_size = (500, 500)  # Size of the frame
# # target_initial_position = np.array([250, 250])  # Initial position of the target
# # target_velocity = np.array([5, 3])  # Constant velocity of the target
# # noise_std = 15  # Standard deviation for motion noise
# #
# # # Initialize particles around the initial position with some noise
# # particles = np.random.normal(target_initial_position, noise_std, (num_particles, 2))
# #
# # # Function to update particles based on a motion model and add noise
# # def predict_particles(particles, velocity, noise_std):
# #     # Move particles based on the given velocity and add noise
# #     particles += velocity + np.random.normal(0, noise_std, particles.shape)
# #     return particles
# #
# # # Function to measure weights based on distance to the target
# # def measure_weights(particles, target_position, noise_std):
# #     # Calculate distance from each particle to the target
# #     distances = np.linalg.norm(particles - target_position, axis=1)
# #     weights = np.exp(-distances ** 2 / (2 * noise_std ** 2))  # Gaussian weighting
# #     weights /= weights.sum()  # Normalize
# #     return weights
# #
# # # Function to resample particles based on weights
# # def resample_particles(particles, weights):
# #     indices = np.random.choice(len(particles), len(particles), p=weights)
# #     resampled_particles = particles[indices]
# #     return resampled_particles
# #
# # # Function to estimate the target position from particles
# # def estimate_position(particles):
# #     return np.mean(particles, axis=0)
# #
# # # Simulation loop
# # num_frames = 100
# # for frame in range(num_frames):
# #     # Create a blank frame
# #     img = np.ones((frame_size[0], frame_size[1], 3), dtype=np.uint8) * 255
# #
# #     # Update target position (simulate target movement)
# #     target_position = target_initial_position + frame * target_velocity
# #
# #     # Predict particle positions with added noise
# #     particles = predict_particles(particles, target_velocity, noise_std)
# #
# #     # Measure weights based on proximity to target
# #     weights = measure_weights(particles, target_position, noise_std)
# #
# #     # Resample particles based on their weights
# #     particles = resample_particles(particles, weights)
# #
# #     # Estimate target position from particles
# #     estimated_position = estimate_position(particles)
# #
# #     # Draw particles, target, and estimated position
# #     for particle in particles:
# #         cv2.circle(img, tuple(particle.astype(int)), 2, (0, 0, 255), -1)  # Particles in red
# #     cv2.circle(img, tuple(target_position.astype(int)), 8, (255, 0, 0), -1)  # Target in blue
# #     cv2.circle(img, tuple(estimated_position.astype(int)), 6, (0, 255, 0), -1)  # Estimated position in green
# #
# #     # Display the frame
# #     cv2.imshow("Particle Filter", img)
# #     if cv2.waitKey(50) & 0xFF == ord('q'):
# #         break
# #
# # cv2.destroyAllWindows()
