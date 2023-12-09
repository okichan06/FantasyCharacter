from diffusers import StableDiffusionPipeline, EulerAncestralDiscreteScheduler
from safetensors import safe_open
import time

def create_image():
    model_id = "./model/AnythingV5Ink_v5PrtRE.safetensors"
    pipe = StableDiffusionPipeline.from_single_file(model_id)
    pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
    # pipe.to("cuda")
    # # pipe.enable_attention_slicing()
    prompt = "masterpiece, best quality, 1man, blue hair, wolf ears, looking at viewer, :3, scarf, jacket, outdoors, forest, slanted eyes"
    negative_prompt = " (deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime:1.4), text, close up, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck,NSFW"
    image = pipe(
        prompt,
        num_inference_steps=10,
        guidance_scale=7,
        width=256,
        height=256,
        negative_prompt=negative_prompt
    ).images[0]
    image.save("result_img.png")
    print("Success saved: result.png")

    if __name__ == "__main__":
        start_time = time.time()
        create_image()
        end_time = time.time()
        print(f"実行時間: {end_time - start_time}秒")