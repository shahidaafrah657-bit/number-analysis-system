import tkinter as tk

# Prime check function
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def analyze_numbers():
    nums = entry.get()

    # Convert input string to list of integers
    try:
        nums = list(map(int, nums.split()))
    except:
        result_label.config(text="⚠ Please enter valid numbers separated by space")
        return

    even = []
    odd = []
    prime = []

    for num in nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

        if is_prime(num):
            prime.append(num)

    total = sum(nums)
    average = total / len(nums)

    result = f"""
Numbers: {nums}

Even: {even}
Odd: {odd}
Prime: {prime}

Sum: {total}
Average: {average:.2f}
"""

    result_label.config(text=result)


# ---------------- GUI DESIGN ----------------

root = tk.Tk()
root.title("Number Analysis System")
root.geometry("500x400")

title = tk.Label(root, text="Number Analysis System", font=("Arial", 16, "bold"))
# title.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), width=40)
entry.pack(pady=10)

btn = tk.Button(root, text="Analyze Numbers", font=("Arial", 12), command=analyze_numbers)
btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

root.mainloop()