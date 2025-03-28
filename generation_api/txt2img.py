from PIL import Image
import requests
import io
import base64
import aiohttp
import asyncio


async def get_data(url, payload):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, json=payload) as response:
            return await response.json(), response.status


async def post_data(url, payload):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:
            return await response.json(), response.status


async def txt2img_generate(prompt_variables_dict):
    if (prompt_variables_dict['hr_checkpoint_name'] == "calicomix.safetensors" or
            prompt_variables_dict['hr_checkpoint_name'] == "grapefruit.safetensors"):
        sampler_name = "DPM++ 2M"
        cfg_scale = "10"
    else:
        sampler_name = "DPM++ SDE"
        cfg_scale = "1"

    payload = {
        "prompt": prompt_variables_dict['prompt'] + ",best quality,digital painting,extremely smooth,"
                                                    "harmonious color scheme,32k,HQ,4K,",
        "negative_prompt": "(worst quality:1.4),(low quality:1.4), easynegative, badhandv4, neg_grapefruit,"
                           "extra fingers, extra arms, extra legs, extra limbs, malformed limbs, missing arms,"
                           "missing legs, missing fingers, fused fingers, too many fingers, long neck, mutated hands,"
                           "mutation, deformed, bad anatomy, bad proportions, cloned face, disfigured, username,"
                           "jpeg artifacts, out of frame, blurry, watermark, signature",
        "seed": -1,
        "sampler_name": sampler_name,
        "batch_size": prompt_variables_dict['batch_size'],
        "steps": 20,
        "cfg_scale": cfg_scale,
        "width": prompt_variables_dict['width'],
        "height": prompt_variables_dict['height'],
        "restore_faces": False,
        "tiling": False,
        "denoising_strength": 0.4,
        "enable_hr": prompt_variables_dict['enable_hr'],
        "hr_scale": 2,
        "hr_upscaler": "4x-UltraSharp",
        "hr_second_pass_steps": 10,
        "hr_checkpoint_name": prompt_variables_dict['hr_checkpoint_name'],
        "hr_sampler_name": sampler_name
    }
    options_payload = {
        "sd_model_checkpoint": prompt_variables_dict['hr_checkpoint_name']
    }
    _, options_response_status = await post_data(f'http://127.0.0.1:7860/sdapi/v1/options', options_payload)

    print(options_response_status)

    txt2img_response_json, txt2img_response_status = await post_data(f'http://127.0.0.1:7860/sdapi/v1/txt2img', payload)

    print(txt2img_response_status)

    result = []

    for i in txt2img_response_json['images']:
        result.append(Image.open(io.BytesIO(base64.b64decode(i.split(",", 1)[0]))))

    return result
