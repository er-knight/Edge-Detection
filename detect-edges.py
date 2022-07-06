import argparse
import cv2
import pathlib

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image-path", required=True)
    parser.add_argument("-f", "--filter", choices=["basic", "blurred", "grayscale", "grayscale-and-blurred"])
    parser.add_argument("-t1", "--threshold1", type=int, default=180)
    parser.add_argument("-t2", "--threshold2", type=int, default=200)
    args = parser.parse_args()

    image_path = pathlib.Path(args.image_path)

    if not image_path.exists():
        print(f"{image_path} doesn't exists.")
        return

    image = cv2.imread(str(image_path))

    if args.filter == "basic":
        canny = cv2.Canny(image, threshold1=args.threshold1, threshold2=args.threshold2)
        image_path = str((image_path.parent / "edges").with_suffix(image_path.suffix))
        cv2.imwrite(image_path, canny)
        print(f"saved at {image_path}!")
        return

    if args.filter == "blurred":
        blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
        canny = cv2.Canny(blurred_image, threshold1=args.threshold1, threshold2=args.threshold2)
        image_path = str((image_path.parent / "edges").with_suffix(image_path.suffix))
        cv2.imwrite(image_path, canny)
        print(f"saved at {image_path}!")
        return

    if args.filter == "grayscale":
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        canny = cv2.Canny(grayscale_image, threshold1=args.threshold1, threshold2=args.threshold2)
        image_path = str((image_path.parent / "edges").with_suffix(image_path.suffix))
        cv2.imwrite(image_path, canny)
        print(f"saved at {image_path}!")
        return

    if args.filter == "grayscale-and-blurred":
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)
        canny = cv2.Canny(blurred_image, threshold1=args.threshold1, threshold2=args.threshold2)
        image_path = str((image_path.parent / "edges").with_suffix(image_path.suffix))
        cv2.imwrite(image_path, canny)
        print(f"saved at {image_path}!")
        return

    print("invalid filter choice")
