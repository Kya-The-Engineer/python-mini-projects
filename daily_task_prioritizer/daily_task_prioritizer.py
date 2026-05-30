"""
"""
def get_tasks():
    print("Daily Task Prioritizer")
    print("----------------------")
    print("Enter your tasks and a priority level for each.")
    print("Use 1 for urgent tasks, 2 for normal tasks, and 3 for low importance tasks.")
    print("When you are done, press Enter on an empty task.")
    print()

    tasks = []

    while True: 
        name = input("Task name (or press Enter to finish).").strip()
        if name == "":
            break 

        priority_text = input("Priority for this task (1 = high, 2 = medium, 3 = low):").strip()

        try:
            priority = int(priority_text)
        except ValueError:
            priority = 2
            print("   Invalid priority. Using 2 (medium) by default.")

        if priority < 1 or priority > 3:
            print("  Priority must be 1,2, or 3.")
            priority = 2

        tasks.append((priority, name))
        print("  Task added.")
        print()

    return tasks

def show_plan(tasks):
    if not tasks:
        print()    
        print("No tasks entered today).") 
        return
    
    # Sort by priority number (1 first, then 2, then 3).
    
    tasks_sorted = sorted(tasks, key=lambda item: item[0])

    # Count how many of each type
    counts = {1: 0, 2: 0, 3: 0}
    for priority, _ in tasks_sorted:
        counts[priority] += 1

        label_map = {
            1: "HIGH   ",
            2: "MEDIUM ",
            3: "LOW    ",
        }

    print()
    print("Here is your plan for today (in order).")
    print("_______________________________________")

    for index, (priority, name) in enumerate(tasks_sorted, start=1):
        label = label_map.get(priority, "MEDIUM")
        print(f"{index}. [{label}] {name}")

    print()
    print("Summary:")
    print(f"  High    priority: {counts[1]}")
    print(f"  Medium  priority: {counts[2]}")
    print(f"  Low     priority: {counts[3]}")
    print(f"  Total tasks:   {len(tasks_sorted)}")
          


def   main():
    tasks = get_tasks()
    show_plan(tasks)


if __name__ == "__main__":
        main()
