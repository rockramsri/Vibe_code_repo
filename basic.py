import math
import random
import json
from datetime import datetime

# comments for better underzrand

class MathOperations:
    def __init__(self):
        self.results = []
        self.operations_performed = 0
        
    def add(self, a, b):
        """Add two numbers"""
        result = a + b
        self.results.append({"operation": "addition", "a": a, "b": b, "result": result})
        self.operations_performed += 1
        return result
    
    def subtract(self, a, b):
        """Subtract two numbers"""
        result = a - b
        self.results.append({"operation": "subtraction", "a": a, "b": b, "result": result})
        self.operations_performed += 1
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers"""
        result = a * b
        self.results.append({"operation": "multiplication", "a": a, "b": b, "result": result})
        self.operations_performed += 1
        return result
    
    def divide(self, a, b):
        """Divide two numbers"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.results.append({"operation": "division", "a": a, "b": b, "result": result})
        self.operations_performed += 1
        return result
    
    def power(self, base, exponent):
        """Calculate power"""
        result = base ** exponent
        self.results.append({"operation": "power", "base": base, "exponent": exponent, "result": result})
        self.operations_performed += 1
        return result
    
    def square_root(self, number):
        """Calculate square root"""
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        result = math.sqrt(number)
        self.results.append({"operation": "square_root", "number": number, "result": result})
        self.operations_performed += 1
        return result
    
    def factorial(self, n):
        """Calculate factorial"""
        if n < 0:
            raise ValueError("Cannot calculate factorial of negative number")
        result = math.factorial(n)
        self.results.append({"operation": "factorial", "n": n, "result": result})
        self.operations_performed += 1
        return result
    
    def generate_random_operations(self, count=10):
        """Generate random math operations"""
        operations = [
            (self.add, "addition"),
            (self.subtract, "subtraction"),
            (self.multiply, "multiplication"),
            (self.divide, "division"),
            (self.power, "power"),
            (self.square_root, "square_root"),
            (self.factorial, "factorial")
        ]
        
        for _ in range(count):
            op_func, op_name = random.choice(operations)
            
            if op_name == "square_root":
                num = random.uniform(0, 100)
                try:
                    op_func(num)
                except ValueError:
                    continue
            elif op_name == "factorial":
                num = random.randint(0, 10)  # Keep factorial small
                try:
                    op_func(num)
                except ValueError:
                    continue
            elif op_name == "division":
                a = random.uniform(-100, 100)
                b = random.uniform(-100, 100)
                if abs(b) < 0.001:  # Avoid division by zero
                    b = 1.0
                try:
                    op_func(a, b)
                except ValueError:
                    continue
            elif op_name == "power":
                base = random.uniform(-10, 10)
                exponent = random.randint(0, 5)  # Keep exponent reasonable
                try:
                    op_func(base, exponent)
                except ValueError:
                    continue
            else:
                a = random.uniform(-100, 100)
                b = random.uniform(-100, 100)
                op_func(a, b)
    
    def generate_files(self):
        """Generate 3 files with different information"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # File 1: Detailed results
        self.generate_results_file(f"math_results_{timestamp}.txt")
        
        # File 2: Statistics
        self.generate_statistics_file(f"math_statistics_{timestamp}.json")
        
        # File 3: Summary
        self.generate_summary_file(f"math_summary_{timestamp}.txt")
        
        print(f"Generated 3 files with timestamp: {timestamp}")
    
    def generate_results_file(self, filename):
        """Generate detailed results file"""
        with open(filename, 'w') as f:
            f.write("MATH OPERATIONS RESULTS\n")
            f.write("=" * 50 + "\n\n")
            
            for i, result in enumerate(self.results, 1):
                f.write(f"Operation {i}:\n")
                f.write(f"  Type: {result['operation']}\n")
                
                if result['operation'] == 'square_root':
                    f.write(f"  Input: {result['number']}\n")
                elif result['operation'] == 'factorial':
                    f.write(f"  Input: {result['n']}\n")
                elif result['operation'] == 'power':
                    f.write(f"  Base: {result['base']}, Exponent: {result['exponent']}\n")
                else:
                    f.write(f"  A: {result['a']}, B: {result['b']}\n")
                
                f.write(f"  Result: {result['result']}\n")
                f.write("-" * 30 + "\n")
    
    def generate_statistics_file(self, filename):
        """Generate statistics file in JSON format"""
        stats = {
            "total_operations": self.operations_performed,
            "operation_counts": {},
            "results_summary": {
                "min_result": float('inf'),
                "max_result": float('-inf'),
                "total_sum": 0,
                "average_result": 0
            }
        }
        
        # Count operations by type
        for result in self.results:
            op_type = result['operation']
            stats["operation_counts"][op_type] = stats["operation_counts"].get(op_type, 0) + 1
            
            # Track min, max, sum
            result_value = result['result']
            if isinstance(result_value, (int, float)):
                stats["results_summary"]["min_result"] = min(stats["results_summary"]["min_result"], result_value)
                stats["results_summary"]["max_result"] = max(stats["results_summary"]["max_result"], result_value)
                stats["results_summary"]["total_sum"] += result_value
        
        # Calculate average
        if self.operations_performed > 0:
            stats["results_summary"]["average_result"] = stats["results_summary"]["total_sum"] / self.operations_performed
        
        # Handle edge cases
        if stats["results_summary"]["min_result"] == float('inf'):
            stats["results_summary"]["min_result"] = None
        if stats["results_summary"]["max_result"] == float('-inf'):
            stats["results_summary"]["max_result"] = None
        
        with open(filename, 'w') as f:
            json.dump(stats, f, indent=2)
    
    def generate_summary_file(self, filename):
        """Generate summary file"""
        with open(filename, 'w') as f:
            f.write("MATH OPERATIONS SUMMARY\n")
            f.write("=" * 30 + "\n\n")
            
            f.write(f"Total operations performed: {self.operations_performed}\n\n")
            
            # Operation counts
            op_counts = {}
            for result in self.results:
                op_type = result['operation']
                op_counts[op_type] = op_counts.get(op_type, 0) + 1
            
            f.write("Operations breakdown:\n")
            for op_type, count in op_counts.items():
                f.write(f"  {op_type.capitalize()}: {count}\n")
            
            f.write("\n" + "=" * 30 + "\n")
            f.write("Program completed successfully!\n")

def main():
    """Main function to run the math operations program"""
    print("Math Operations Program")
    print("=" * 30)
    
    # Create math operations instance
    math_ops = MathOperations()
    
    # Perform some sample operations
    print("Performing sample operations...")
    math_ops.add(10, 5)
    math_ops.subtract(20, 7)
    math_ops.multiply(4, 6)
    math_ops.divide(15, 3)
    math_ops.power(2, 8)
    math_ops.square_root(25)
    math_ops.factorial(5)
    
    # Generate random operations
    print("Generating random operations...")
    math_ops.generate_random_operations(15)
    
    # Generate the 3 files
    print("Generating files...")
    math_ops.generate_files()
    
    print("Program completed!")

if __name__ == "__main__":
    main()
