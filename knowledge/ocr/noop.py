class NoopOCR:

    def extract_text(
        self,
        image_path: str,
    ) -> str:

        raise NotImplementedError(
            "OCR 当前未启用，请配置 OCR 引擎"
        )