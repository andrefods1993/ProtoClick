import google.generativeai as genai

genai.configure(api_key="AIzaSyA1-8n1KHlvwVzZWMSAiej3l1h6pc4o5zQ")

def formatar_texto_genai(texto_original):
    generation_config = genai.GenerationConfig(
        temperature=1,
        top_p=1,
        top_k=1,
        max_output_tokens=2048,
    )

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

    convo = model.start_chat(history=[
    {
        "role": "user",
        "parts": ["Vamos usar essa conversa pra melhorar texto para um relatório, corrigindo a ortografia e deixando mais claro e objetivo, facilitantando para quem está lendo, organizando colocando em tópicos Objetivo, Resumo e Conclusão. Retornando somente texto tratado em um formato padrão, vamos utilizar o seguinte dados \"Data: \", \"Cliente: \", \"Tipo de Atendimento: \"."]
    },
    {
        "role": "model",
        "parts": ["**Relatório**\n\n**Data:**\n**Cliente:**\n**Tipo de Atendimento:**\n\n**Objetivo**\n\n* Descrever os resultados do atendimento prestado ao cliente.\n\n**Resumo**\n\n* Fornecer um resumo dos principais pontos do atendimento, incluindo:\n    * Razão do contato\n    * Ações tomadas\n    * Resultado obtido\n\n**Conclusão**\n\n* Resumir as conclusões tiradas do atendimento e quaisquer recomendações para ações futuras."]
    },
    ])

    resposta_genai = convo.send_message(texto_original)
    texto_formatado = resposta_genai._result.candidates[0].content.parts[0].text
    return texto_formatado