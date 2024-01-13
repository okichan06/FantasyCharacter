from diffusers import StableDiffusionPipeline, EulerAncestralDiscreteScheduler
from safetensors import safe_open
import time

def create_image(prompt):
    try:
        model_id = "./model/AnythingV5Ink_v5PrtRE.safetensors"
        pipe = StableDiffusionPipeline.from_single_file(model_id)
        pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
        # pipe.to("cuda")
        # # pipe.enable_attention_slicing()
        prompt = prompt
        negative_prompt = " ((NSFW)),(deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime:1.4), text, close up, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck"
        
        if pipe.safety_checker is not None:
                pipe.safety_checker = lambda images, **kwargs: (images, None)
        pipe.enable_attention_slicing()
        

        image = pipe(
            prompt,
            num_inference_steps=20,
            guidance_scale=7,
            width=360,
            height=360,
            negative_prompt=negative_prompt
        ).images[0]
        image.save("static/images/result_img.png")
        return True, "result_img.png"
    except Exception as e:
         return False,str(e)

if __name__ == "__main__":
    prompt=input()
    start_time = time.time()
    create_image(prompt)
    end_time = time.time()
    print(f"実行時間: {end_time - start_time}秒")