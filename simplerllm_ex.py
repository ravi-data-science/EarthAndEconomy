from simplerllm.language.llm import LLM, LLMProvider

# Create an LLM instance for LLaMA
llm_instance = LLM.create(provider=LLMProvider.LLaMA, model_name="llama-2")

# Define the prompt
prompt = "What is the capital of France?"

# Generate a response
response = llm_instance.generate_response(prompt=prompt)

# Print the response
print("Response:", response)
