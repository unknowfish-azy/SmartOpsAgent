class TesseractOCR:
    """
    基于 Tesseract 的 OCR 实现。

    外部 OCR 引擎调用已临时注释：pytesseract / Pillow 以及本机
    Tesseract 属于可选依赖，缺少时会直接崩溃，因此改为模拟返回。
    """

    def __init__(
        self,
        lang: str = "chi_sim+eng",
    ):
        self.lang = lang

    def extract_text(
        self,
        image_path: str,
    ) -> str:

        # 【此处为外部 OCR 引擎调用，已临时注释，后续填入密钥即可恢复】
        # import pytesseract
        # from PIL import Image
        #
        # image = Image.open(image_path)
        # return pytesseract.image_to_string(
        #     image,
        #     lang=self.lang,
        # )

        # 模拟占位返回：避免缺少 OCR 引擎时程序崩溃。
        return (
            f"[OCR 模拟结果] 未启用真实 OCR 引擎，"
            f"图片路径：{image_path}"
        )
