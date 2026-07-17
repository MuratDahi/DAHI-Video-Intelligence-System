import torch
import open_clip


class ClipModel:

    def __init__(self):

        self.device = (
            "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )

        print(f"Device : {self.device}")

        self.model, _, self.preprocess = open_clip.create_model_and_transforms(

            "ViT-B-32",

            pretrained="laion2b_s34b_b79k"

        )

        self.model.to(self.device)

        self.model.eval()

        self.tokenizer = open_clip.get_tokenizer(
            "ViT-B-32"
        )