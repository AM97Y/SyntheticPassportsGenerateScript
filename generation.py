from argparse import ArgumentParser
from datetime import datetime
from tqdm import tqdm

from ImageCreator import ImageCreator
from Passport import PassportContent, PassportAppearance
from utils.path_utils import Paths

print(tqdm)
def generate_path(count_examples, output):
    """
    Generate path of passport images.

    """
    passport_content = PassportContent()
    passport_appearance = PassportAppearance()

    for i in tqdm(range(0, count_examples)):
        passport_content.random_init()
        passport_appearance.font_pick = passport_content.font_pick
        passport_appearance.random_init()

        img_creator = ImageCreator(passport_content.content, passport_appearance.content)
        img = img_creator.create_image()

        img_filepath = Paths.outputs(output) / f'{datetime.now().strftime("%Y-%m-%d-%H.%M.%S.%f")}.png'
        img.save(str(img_filepath))

        del img, img_creator, img_filepath


def init_argparse():
    """
    Initializes argparse
    Returns parser.

    """
    parser = ArgumentParser(description='Aug')

    parser.add_argument(
        '--output_path',
        nargs='?',
        help='Path to save files',
        default='./passports_gen/',
        type=str)
    parser.add_argument(
        '--count',
        nargs='?',
        help='Number of generated passports',
        default=2,
        type=int)

    return parser


if __name__ == "__main__":
    args = init_argparse().parse_args()
    generate_path(args.count, args.output_path)