import csv

def csv_to_document(csv_file_path, output_file_path):
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader, None)
        
        with open(output_file_path, 'w', encoding='utf-8') as doc_file:
            if headers:
                doc_file.write("Headers:\n")
                doc_file.write(', '.join(headers) + '\n\n')
                doc_file.write("Content:\n")
            
            row_number = 1
            for row in csv_reader:
                doc_file.write(f"Row {row_number}:\n")
                if headers:
                    for i, (header, value) in enumerate(zip(headers, row)):
                        doc_file.write(f"{header}: {value}\n")
                else:
                    doc_file.write(', '.join(row) + '\n')
                doc_file.write('\n')
                row_number += 1
            print("All done! Check your new file!")

if __name__ == "__main__":
    input_csv = "iris_missing_outliers.csv"  # Change this to your CSV file name
    output_doc = "mydata.txt"  # Change this to your new file name
    csv_to_document(input_csv, output_doc)