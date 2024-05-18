This is a sample project made in python to generate QR codes. It uses libraries like `qrcode` and `Pillow` module.

Some features and functions of the module `qrcode` are:

-   **Version**: This parameter is an integer from 1 to 40 that controls the size of the QR Code (the smallest, version 1, is a 21×21 matrix).
-   **error_correction**: Error correction allows the QR Code to remain scannable even if a portion of it is partially obscured or damaged. QR codes come with four levels of error correction – Low (L) – 7%, Medium (M)- 15%, Quartile (Q) – 25%, and High (H) – 30%.
    -   `qrcode.constants.ERROR_CORRECT_[LMQH]` : About 7% or fewer errors can be corrected.
    -   `qrcode.constants.ERROR_CORRECT_[LMQH]` (default) : About 15% or fewer errors can be corrected.
    -   `qrcode.constants.ERROR_CORRECT_[LMQH]`: About 25% or fewer errors can be corrected.
    -   `qrcode.constants.ERROR_CORRECT_[LMQH]`: About 30% or fewer errors can be corrected.
-   **box_size**: This parameter controls how many pixels each “box” of the QR code is.
-   **border**: The border parameter controls how many boxes thick the border should be (the default is 4, which is the minimum in the specification).
-   **add_data()**: This method is used to add data to the QRCode object. It takes the data to be encoded as a parameter.
-   **make()**: This method with (fit=True) ensures that the entire dimension of the QR Code is utilized, even if our input data could fit into less number of boxes.
-   **make_image()**: This method is used to convert the QRCode object into an image file. It takes the fill_color and back_color optional parameters to set the foreground and background color.

---

Some features and functions of the module `Pillow` are:

-   The Python Imaging Library adds image processing capabilities to your Python interpreter.

-   This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities.

-   The core image library is designed for fast access to data stored in a few basic pixel formats. It should provide a solid foundation for a general image processing tool.
