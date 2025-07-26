import tkinter as tk
import math
import random

# --- Configuration ---
WIDTH = 600
HEIGHT = 600
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2
ANIMATION_DELAY_MS = 20
TIME_STEP = 0.03

# --- Solar System Data ---
sun_radius = 18
sun_color = "yellow"

planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planet_radii = [6, 7, 8, 8, 10, 9, 8, 8]
planet_colors = ["gray", "orange", "blue", "red", "orange4", "gold", "lightblue", "darkblue"]
orbital_radii = [40, 65, 90, 115, 150, 185, 215, 240]
orbital_speeds = [0.3, 0.22, 0.18, 0.15, 0.07, 0.06, 0.04, 0.03]
current_orbital_angles = [0.0] * len(planet_radii)

# Earth and Moon
earth_index = 2
moon_radius = 3
moon_color = "lightgray"
moon_orbital_radius = 14
moon_orbital_speed = 1
moon_current_angle = 0.0

# Star field
NUM_STARS = 150
stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_STARS)]

# --- Tkinter Setup ---
root = tk.Tk()
root.title("Solar System - Realistic Orbit")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# --- Drawing Function ---
def draw_solar_system():
    canvas.delete("all")

    # Draw stars
    for x, y in stars:
        canvas.create_oval(x, y, x + 1, y + 1, fill="white", outline="white")

    # Draw the Sun
    canvas.create_oval(
        CENTER_X - sun_radius, CENTER_Y - sun_radius,
        CENTER_X + sun_radius, CENTER_Y + sun_radius,
        fill=sun_color, outline=sun_color
    )
    canvas.create_text(CENTER_X, CENTER_Y - sun_radius - 10, text="Sun", fill="white", font=("Arial", 8, "bold"))

    # Draw each planet
    for i in range(len(planet_radii)):
        orbit_radius = orbital_radii[i]
        angle = current_orbital_angles[i]

        # Orbit path
        canvas.create_oval(
            CENTER_X - orbit_radius, CENTER_Y - orbit_radius,
            CENTER_X + orbit_radius, CENTER_Y + orbit_radius,
            outline="gray", width=0.5, dash=(2, 2)
        )

        # Planet position
        x = CENTER_X + orbit_radius * math.cos(angle)
        y = CENTER_Y + orbit_radius * math.sin(angle)
        r = planet_radii[i]

        # Draw planet
        canvas.create_oval(
            x - r, y - r,
            x + r, y + r,
            fill=planet_colors[i], outline=planet_colors[i]
        )

        # Draw planet name above
        canvas.create_text(x, y - r - 10, text=planet_names[i], fill="white", font=("Arial", 7))

        # Draw Earth’s Moon
        if i == earth_index:
            x_moon = x + moon_orbital_radius * math.cos(moon_current_angle)
            y_moon = y + moon_orbital_radius * math.sin(moon_current_angle)

            # Moon orbit
            canvas.create_oval(
                x - moon_orbital_radius, y - moon_orbital_radius,
                x + moon_orbital_radius, y + moon_orbital_radius,
                outline="darkgray", width=0.3, dash=(1, 1)
            )

            # Draw Moon
            canvas.create_oval(
                x_moon - moon_radius, y_moon - moon_radius,
                x_moon + moon_radius, y_moon + moon_radius,
                fill=moon_color, outline=moon_color
            )
            # Moon label
            canvas.create_text(x_moon, y_moon - moon_radius - 8, 
                               text="Moon", fill="white", font=("Arial", 6))

# --- Animation ---
def animate():
    global current_orbital_angles, moon_current_angle

    for i in range(len(planet_radii)):
        current_orbital_angles[i] += orbital_speeds[i] * TIME_STEP
        current_orbital_angles[i] %= 2 * math.pi

    moon_current_angle += moon_orbital_speed * TIME_STEP
    moon_current_angle %= 2 * math.pi

    draw_solar_system()
    root.after(ANIMATION_DELAY_MS, animate)

# --- Start ---
draw_solar_system()
animate()
root.mainloop()


"""
# without label
import tkinter as tk
import math
import random

# --- Configuration ---
WIDTH = 600
HEIGHT = 600
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2
ANIMATION_DELAY_MS = 20
TIME_STEP = 0.03

# --- Solar System Data ---
sun_radius = 18
sun_color = "yellow"

# Planet names (re-added for completeness, matches other planet data lists)
planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Increased planet sizes (except Sun)
planet_radii = [6, 7, 8, 8, 10, 9, 8, 8]
planet_colors = ["gray", "orange", "blue", "red", "orange4", "gold", "lightblue", "darkblue"]
orbital_radii = [40, 65, 90, 115, 150, 185, 215, 240]
orbital_speeds = [0.3, 0.22, 0.18, 0.15, 0.07, 0.06, 0.04, 0.03]

# Initial angles
current_orbital_angles = [0.0] * len(planet_radii)

# Earth and Moon
earth_index = 2
moon_radius = 3  # slightly increased
moon_color = "lightgray"
moon_orbital_radius = 14
moon_orbital_speed = 1
moon_current_angle = 0.0

# Star field
NUM_STARS = 150
stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_STARS)]

# --- Tkinter Setup ---
root = tk.Tk()
root.title("Solar System - Realistic Orbit")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# --- Drawing Function ---
def draw_solar_system():
    canvas.delete("all")

    # Draw stars
    for x, y in stars:
        canvas.create_oval(x, y, x + 1, y + 1, fill="white", outline="white")

    # Draw the Sun
    canvas.create_oval(
        CENTER_X - sun_radius, CENTER_Y - sun_radius,
        CENTER_X + sun_radius, CENTER_Y + sun_radius,
        fill=sun_color, outline=sun_color
    )

    for i in range(len(planet_radii)):
        orbit_radius = orbital_radii[i]
        angle = current_orbital_angles[i]

        # Planet orbit path
        canvas.create_oval(
            CENTER_X - orbit_radius, CENTER_Y - orbit_radius,
            CENTER_X + orbit_radius, CENTER_Y + orbit_radius,
            outline="gray", width=0.5, dash=(2, 2)
        )

        # Planet position
        x = CENTER_X + orbit_radius * math.cos(angle)
        y = CENTER_Y + orbit_radius * math.sin(angle)
        r = planet_radii[i]

        canvas.create_oval(
            x - r, y - r,
            x + r, y + r,
            fill=planet_colors[i], outline=planet_colors[i]
        )

        # Draw Moon orbiting Earth
        if i == earth_index:
            x_moon = x + moon_orbital_radius * math.cos(moon_current_angle)
            y_moon = y + moon_orbital_radius * math.sin(moon_current_angle)

            canvas.create_oval(
                x - moon_orbital_radius, y - moon_orbital_radius,
                x + moon_orbital_radius, y + moon_orbital_radius,
                outline="darkgray", width=0.3, dash=(1, 1)
            )
            canvas.create_oval(
                x_moon - moon_radius, y_moon - moon_radius,
                x_moon + moon_radius, y_moon + moon_radius,
                fill=moon_color, outline=moon_color
            )

# --- Animation ---
def animate():
    global current_orbital_angles, moon_current_angle

    for i in range(len(planet_radii)):
        current_orbital_angles[i] += orbital_speeds[i] * TIME_STEP
        current_orbital_angles[i] %= 2 * math.pi

    moon_current_angle += moon_orbital_speed * TIME_STEP
    moon_current_angle %= 2 * math.pi

    draw_solar_system()
    root.after(ANIMATION_DELAY_MS, animate)

# --- Start ---
draw_solar_system()
animate()
root.mainloop() 
"""