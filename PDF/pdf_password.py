import pikepdf
import os


if __name__ == "__main__":
    directory_path = os.getcwd()
    print(__name__, directory_path)

    file_name=r"D:\Distribs\Driver\Yamaha MCR-N560D\CRX-N560_N560D_om_G1-1_EnFrDeNl.pdf"

    # remove_password_from_pdf
    with pikepdf.open(file_name) as pdf:
        print(len(pdf.pages))
        pdf = pikepdf.open(file_name, allow_overwriting_input=True)
        del pdf.pages[45:]
        print(len(pdf.pages))

        pdf.save(os.path.join(directory_path, 'output.pdf'))
