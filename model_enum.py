from enum import Enum


class Model(Enum):
	ANALOG = ("analog-diffusion-1.0.ckpt [9ca13f02]", "Analog V1", "01")
	ANYTHING_V3 = ("anythingv3_0-pruned.ckpt [2700c435]", "Anything V3", "02")
	ANYTHING_V4 = ("anything-v4.5-pruned.ckpt [65745d25]", "Anything V4.5", "03")
	ABYSSORANGEMIX = ("AOM3A3_orangemixs.safetensors [9600da17]",
	                  "AbyssOrangeMix V3", "04")
	DELIBERATE = ("deliberate_v2.safetensors [10ec4b29]", "Deliberate V2", "05")
	DREAMLIKE_V1 = ("dreamlike-diffusion-1.0.safetensors [5c9fd6e0]",
	                "Dreamlike Diffusion V1", "06")
	DREAMLIKE_V2 = ("dreamlike-diffusion-2.0.safetensors [fdcf65e7]",
	                "Dreamlike Diffusion V2", "07")
	DREAMSHAPER_5 = ("dreamshaper_5BakedVae.safetensors [a3fbf318]",
	                 "Dreamshaper 5 baked vae", "08")
	DREAMSHAPER_6 = ("dreamshaper_6BakedVae.safetensors [114c8abb]",
	                 "Dreamshaper 6 baked vae", "09")
	ELLDRETHVIVIDMIX = ("elldreths-vivid-mix.safetensors [342d9d26]",
	                    "Elldreth's Vivid", "10")
	LYRIEL_V15 = ("lyriel_v15.safetensors [65d547c5]", "Lyriel V1.5", "11")
	LYRIEL_V16 = ("lyriel_v16.safetensors [68fceea2]", "Lyriel V1.6", "12")
	MECHAMIX = ("mechamix_v10.safetensors [ee685731]", "MechaMix V1.0", "13")
	MEINAMIX = ("meinamix_meinaV9.safetensors [2ec66ab0]", "MeinaMix V9", "14")
	OPENJOURNEY = ("openjourney_V4.ckpt [ca2f377f]", "Openjourney V4", "15")
	PORTRAIT = ("portrait+1.0.safetensors [1400e684]", "Portrait V1", "16")
	REALISTICVS_V14 = ("Realistic_Vision_V1.4-pruned-fp16.safetensors [8d21810b]",
	                   "Realistic Vision V1.4", "17")
	REALISTICVS_V20 = ("Realistic_Vision_V2.0.safetensors [79587710]",
	                   "Realistic Vision V2.0", "18")
	REV_ANIMATED = ("revAnimated_v122.safetensors [3f4fefd9]",
	                "ReV Animated V1.2.2", "19")
	RIFFUSION = ("riffusion-model-v1.ckpt [3aafa6fe]", "Riffusion V1", "20")
	SD_V14 = ("sdv1_4.ckpt [7460a6fa]", "Stable Diffusion V1.4", "21")
	SD_V15 = ("v1-5-pruned-emaonly.ckpt [81761151]", "Stable Diffusion V1.5",
	          "22")
	SBP = ("shoninsBeautiful_v10.safetensors [25d8c546]",
	       "Shonin's Beautiful People V1.0", "23")
	THEALLYSMIX = ("theallys-mix-ii-churned.safetensors [5d9225a4]",
	               "TheAlly's Mix II", "24")
	TIMELESS = ("timeless-1.0.ckpt [7c4971d4]", "Timeless V1", "25")


class Ratio(Enum):
	SQUARE = ('square', "01")
	PORTRAIT = ('portrait', "02")
	LANDSCAPE = ('landscape', "03")


class Control(Enum):
	SOFT_EDGE = ("control_v11p_sd15_softedge [a8575a2a]", "Soft Edge", "01")
	MLSD = ("control_v11p_sd15_mlsd [aca30ff0]", "MLSD", "02")
	IP2P = ("control_v11e_sd15_ip2p [c4bb465c]", "IP2P", "03")
	SEG = ("control_v11p_sd15_seg [e1f51eb9]", "Segmentation", "04")
	INPAINT = ("control_v11p_sd15_inpaint [ebff9138]", "Inpaint", "05")
	LINEART_ANIME = ("control_v11p_sd15s2_lineart_anime [3825e83e]",
	                 "Line Art Anime", "06")
	SHUFFLE = ("control_v11e_sd15_shuffle [526bfdae]", "Shuffle", "07")
	CANNY = ("control_v11p_sd15_canny [d14c016b]", "Canny", "08")
	LINEART = ("control_v11p_sd15_lineart [43d4be0d]", "Line Art", "09")
	NORMALBAE = ("control_v11p_sd15_normalbae [316696f1]", "Normal BAE", "10")
	DEPTH = ("control_v11f1p_sd15_depth [cfd03158]", "Depth", "11")
	OPENPOSE = ("control_v11p_sd15_openpose [cab727d4]", "Open Pose", "12")
	TILE = ("control_v11f1e_sd15_tile [a371b31b]", "Tile", "13")
	SCRIBBLE = ("control_v11p_sd15_scribble [d4ba51ff]", "Scribble", "14")


class Sampler(Enum):
	EULER = ("Euler", "01")
	EULER_A = ("Euler a", "02")
	HEUN = ("Heun", "03")
	DPM_2M_KARRAS = ("DPM++ 2M Karras", "04")
	DDIM = ("DDIM", "05")
