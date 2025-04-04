import os

class Project:
    project_path = os.path.dirname(os.path.abspath(__file__))

    # Đường dẫn đến thư mục chứa dữ liệu CASIA-B
    casia_root = os.path.join(project_path, "casia_b", "output")

    # Kiểm tra xem thư mục gốc có tồn tại không
    if not os.path.exists(casia_root):
        raise FileNotFoundError(f"❌ Không tìm thấy thư mục dữ liệu CASIA-B tại: {casia_root}")

    # Đường dẫn đến ảnh trong bộ CASIA-B
    test_data_path = os.path.join(casia_root, "001", "nm-01", "000", "001-nm-01-000-001.png")

    # Đường dẫn đến bộ dữ liệu CASIA-B (có thể dùng để load dataset)
    casia_dataset_b_path = os.path.join(casia_root, "001", "nm-02", "000", "001-nm-02-000-001.png")

    # Ảnh kiểm thử (một ảnh khác của ID 002)
    casia_test_img = os.path.join(casia_root, "002", "nm-01", "000", "002-nm-01-000-001.png")

    # Đường dẫn thư mục ảnh kiểm thử (ID 003)
    casia_test_img_dir = os.path.join(casia_root, "003", "nm-01", "000")

    # Kiểm tra xem các file/directory có tồn tại không
    for path in [test_data_path, casia_dataset_b_path, casia_test_img]:
        if not os.path.exists(path):
            raise FileNotFoundError(f"❌ Không tìm thấy file: {path}")

    # Đảm bảo thư mục lưu ảnh kiểm thử tồn tại
    os.makedirs(casia_test_img_dir, exist_ok=True)

if __name__ == '__main__':
    print(f"✅ Project Path: {Project.project_path}")
    print(f"✅ CASIA-B Path: {Project.casia_root}")
