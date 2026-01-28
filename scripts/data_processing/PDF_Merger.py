import os
from PyPDF2 import PdfMerger

def merge_pdfs(folder_path, output_file="merged.pdf"):
    """
    Merges all PDF files from the specified folder into a single PDF file.

    Args:
        folder_path (str): Path to the folder containing PDF files to merge.
        output_file (str, optional): Name (or path) of the output merged PDF file.
            Defaults to 'merged.pdf'.

    Returns:
        None

    Example:
        >>> merge_pdfs("C:/Users/Sahithi/Documents/PDFs", output_file="combined.pdf")
        PDFs merged successfully and saved as 'combined.pdf'
    """

    # Check if the folder exists
    if not os.path.exists(folder_path):
        print("❌ The specified folder does not exist.")
        return

    merger = PdfMerger()
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]

    if not pdf_files:
        print("⚠️ No PDF files found in the specified folder.")
        return

    # Sort PDF files alphabetically for consistent merging order
    pdf_files.sort()

    # Append each PDF file to the merger
    for file in pdf_files:
        file_path = os.path.join(folder_path, file)
        merger.append(file_path)
        print(f"➕ Added: {file}")

    # Write all merged content to the output file
    merger.write(output_file)
    merger.close()

    print(f"✅ PDFs merged successfully into '{output_file}'.")


if __name__ == "__main__":
    # Ask user for folder path and output file name
    folder = input("Enter the folder path containing PDFs: ").strip()
    output = input("Enter output file name (default: merged.pdf): ").strip() or "merged.pdf"
    merge_pdfs(folder, output)
