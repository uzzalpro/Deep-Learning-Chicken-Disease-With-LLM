from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

from langchain.schema import AIMessage
# Set Hugging Face API token
def get_llm_explanation(image_caption):
    
    if image_caption.lower() == "healthy":
        return "No disease detected. The chicken appears healthy."
    llm = HuggingFaceEndpoint(
        repo_id="deepseek-ai/DeepSeek-R1",
        provider="together"
    )
    model = ChatHuggingFace(llm=llm)

    # Make the prompt
    prompt = f"You are an expert veterinarian. Explain the cause, symptoms, prevention, and treatment for a chicken based on this image description: {image_caption}"

    # Get AIMessage object
    result_message = model.invoke(prompt)

    # Extract text content
    if isinstance(result_message, AIMessage):
        return result_message.content
    else:
        return str(result_message)


# Test run
# if __name__ == "__main__":
#     print(get_llm_explanation("Coccidiosis"))












# if __name__ == "__main__":
#     print(get_llm_explanation("Coccidiosis"))




# from langchain_ollama import ChatOllama
# from langchain.prompts import ChatPromptTemplate
# from langchain.schema import StrOutputParser

# # Initialize local free model
# llm = ChatOllama(model="llama3")  # you can also use "mistral" or "phi3"

# prompt = ChatPromptTemplate.from_template("""
# You are a poultry veterinary assistant.
# The disease prediction is: {diagnosis}.
# Explain in detail:
# 1. What this means for chickens.
# 2. Symptoms and effects.
# 3. Recommended treatments and prevention steps.
# 4. Give both English and Bangla versions clearly.
# """)

# chain = prompt | llm | StrOutputParser()

# def get_llm_explanation(diagnosis):
#     return chain.invoke({"diagnosis": diagnosis})



# llm_agent/agent.py
# from openai import OpenAI
# import os

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def get_llm_response(diagnosis: str):
#     prompt = f"""
#     You are a poultry veterinary assistant.
#     The diagnosis is: {diagnosis}.
#     Explain what it means for the chicken,
#     how to treat it, and how to prevent it.
#     Answer in English and Bangla.
#     """
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response.choices[0].message.content


# # llm_agent/agent.py
# from langchain.chat_models import ChatOpenAI
# from langchain.prompts import ChatPromptTemplate
# from langchain.schema import StrOutputParser

# llm = ChatOpenAI(model="gpt-4o-mini")

# prompt = ChatPromptTemplate.from_template("""
# You are an AI veterinary assistant.
# Given this diagnosis: {diagnosis},
# 1. Explain what it means.
# 2. Suggest treatment and prevention.
# 3. Translate to Bangla.
# """)

# chain = prompt | llm | StrOutputParser()

# def get_llm_explanation(diagnosis):
#     return chain.invoke({"diagnosis": diagnosis})
