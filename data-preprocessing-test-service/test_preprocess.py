import requests
import config


def test_data_preprocessing_service():
    """Test the data preprocessing service."""
    url = config.DATA_PREPROCESSING_SERVICE_URL + '/preprocess-coco'
    response = requests.get(url)
    assert response.status_code == 200
    assert "success" in response.json().get("status")
    print("Data preprocessing service test passed.")


if __name__ == "__main__":
    test_data_preprocessing_service()
