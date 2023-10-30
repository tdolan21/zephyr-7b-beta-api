from fastapi import FastAPI, HTTPException, Body
from transformers import pipeline
import torch

torch.cuda.empty_cache()


app = FastAPI()

pipe = pipeline("text-generation", model="HuggingFaceH4/zephyr-7b-beta", torch_dtype=torch.bfloat16, device_map="auto")

@app.post("/generate/")
async def generate_text(data: dict):
    messages = data["messages"]
    temperature = data.get("temperature", 0.7)
    top_k = data.get("top_k", 50)
    top_p = data.get("top_p", 0.95)
    
    try:
        prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        outputs = pipe(prompt, max_new_tokens=256, do_sample=True, temperature=temperature, top_k=top_k, top_p=top_p)
        return {"response": outputs[0]["generated_text"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
