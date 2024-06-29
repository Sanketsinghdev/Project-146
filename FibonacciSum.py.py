import tkinter as tk

# Function to generate Fibonacci Series and update labels
def generate_fibonacci():
    # Get input from user
    try:
        n = int(entry.get())
    except ValueError:
        return

    # Initialize variables
    first_num, second_num = 0, 1
    sum1, sum2 = 0, 0
    fib_series = []
    
    # Generate Fibonacci Series and calculate sum
    while n > 0:
        fib_series.append(first_num)
        sum2 += first_num
        next_num = first_num + second_num
        first_num = second_num
        second_num = next_num
        n -= 1
    
    # Update Fibonacci Series Label
    fib_label.config(text="Fibonacci Series: " + ", ".join(map(str, fib_series)))
    
    # Update Sum of Fibonacci Numbers Label
    sum_label.config(text=f"Sum of Fibonacci Numbers: {sum2}")

# Create root window
root = tk.Tk()
root.title("Fibonacci Series Generator")

# Set dimensions of the window
root.geometry("400x300")

# Create Entry widget
entry = tk.Entry(root, width=20)
entry.pack(pady=10)

# Create Button widget
btn_generate = tk.Button(root, text="Generate Fibonacci", command=generate_fibonacci, fg="white", bg="blue")
btn_generate.pack()

# Create Labels
fib_label = tk.Label(root, text="Fibonacci Series will be displayed here", wraplength=300)
fib_label.pack(pady=10)

sum_label = tk.Label(root, text="Sum of Fibonacci Numbers will be displayed here")
sum_label.pack()

# Start the Tkinter event loop
root.mainloop()

