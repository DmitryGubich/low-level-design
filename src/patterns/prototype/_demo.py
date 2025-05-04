from patterns.prototype.docs import Document

if __name__ == "__main__":
    images = ["Image1.png"]
    annotations = ["Annotation1"]

    original_doc = Document("Hello, World!", images, "Basic", annotations)

    # Cloning the document using the prototype pattern
    copied_doc = original_doc.clone_document()

    # Making changes to the original document
    original_doc.add_image("Image2.png")
    original_doc.add_annotation("Annotation2")

    # Displaying the contents of both documents
    print("Original Document:")
    original_doc.display()
    print("\nCopied Document:")
    copied_doc.display()
