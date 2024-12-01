import sys

# Print Python path to ensure correct environment
print("Python executable path:", sys.executable)

# Check for simplerllm
try:
    import simplerllm
    print("SimplerLLM is installed and recognized.")
except ImportError:
    print("SimplerLLM is not recognized. Check your installation and environment.")

