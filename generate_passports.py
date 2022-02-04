from argparse import ArgumentParser
from datetime import datetime

from pathlib import Path
from tqdm import tqdm

from ImageCreator import ImageCreator
from Passport import PassportContent, PassportAppearance


def generate_synthetic_images(save_dir, count_images):
    """
        Generate synthetic RF passport images

        :param save_dir: path to save generated synthetic images
        :param count_images: count of images to generate
    """
    passport_content = PassportContent()
    passport_appearance = PassportAppearance()

    Path(save_dir).mkdir(parents=True, exist_ok=True)

    for _ in tqdm(range(0, count_images)):
        passport_content.random_init()
        passport_appearance.font_pick = passport_content.font_pick
        passport_appearance.random_init()

        img = ImageCreator(passport_content.content, passport_appearance.content).create_image() # synthetic image

        img_filepath = Path(save_dir) / f'{datetime.now().strftime("%Y-%m-%d-%H.%M.%S.%f")}.png'
        img.save(str(img_filepath))

        del img, img_filepath


def init_argparse():
    """
        Initializes argparse

        :return: parser
    """
    parser = ArgumentParser(description='Generate synthetic images of RF passports')
    parser.add_argument(
        '--output_path',
        '-o',
        nargs='?',
        help='Path to save synthetic images',
        default='./synthetic_passports/',
        type=str)
    parser.add_argument(
        '--number_images',
        '-n',
        nargs='?',
        help='Number of synthetic images to generate',
        default=2,
        type=int)
    return parser


if __name__ == "__main__":
    args = init_argparse().parse_args()
    generate_synthetic_images(save_dir=args.output_path, count_images=args.number_images)