import random

class Partition:
    def __init__(self, partition_id, size):
        self.partition_id = partition_id  # Partition identifier (e.g., P1, P2, etc.)
        self.size = size  # Size of the partition in KB
        self.used = 0  # Amount of memory used in this partition (initially 0)

    def is_available(self, required_size):
        """Checks if the partition has enough space available."""
        return self.size - self.used >= required_size

    def allocate(self, size):
        """Allocate the specified size in the partition if space is available."""
        if self.is_available(size):
            self.used += size
            return True
        return False

    def __str__(self):
        """Displays the partition's status."""
        return f"Partition {self.partition_id}: {self.size}KB, Used: {self.used}KB, Free: {self.size - self.used}KB"


class FirstFitAllocator:
    def __init__(self, partitions):
        self.partitions = partitions  # List of Partition objects

    def allocate(self, job_id, size):
        """Allocate memory to the job using the First Fit strategy."""
        for partition in self.partitions:
            if partition.allocate(size):
                print(f"Job {job_id} ({size}KB) allocated to {partition.partition_id}.")
                return True
            else:
                # If a partition doesn't have enough space, print a message
                print(f"Partition {partition.partition_id} does not have enough space for Job {job_id} ({size}KB).")

        # If no partition could allocate, print that partitions have not enough space
        print("Partitions have not enough space.")
        return False

    def display_memory(self):
        """Display the status of all memory partitions."""
        for partition in self.partitions:
            print(partition)


# Example Usage
def main():
    # Creating 5 partitions with different sizes
    partitions = [
        Partition("P1", 3000),  # 3KB
        Partition("P2", 5000),  # 5KB
        Partition("P3", 4000),  # 4KB
        Partition("P4", 6000),  # 6KB
        Partition("P5", 7000),  # 7KB
    ]

    allocator = FirstFitAllocator(partitions)

    # Simulating jobs 1 to 5 with random memory sizes between 1000KB and 6500KB
    jobs = [(job_id, random.randint(1000, 6500)) for job_id in range(1, 6)]
    print("Jobs with sizes (KB):", jobs)

    for job_id, size in jobs:
        print(f"\nAllocating memory for Job {job_id} ({size}KB):")
        allocated = allocator.allocate(job_id, size)
        allocator.display_memory()


if __name__ == "__main__":
    main()
