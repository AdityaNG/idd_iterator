
def test_idd_multimodal():
    from idd_iterator import idd_multimodal_iterator
    import numpy as np
    import pandas as pd
    multimodal_iter = idd_multimodal_iterator.IDDMultimodalIterator(
        idd_multimodal_path="idd_multimodal_mini/",
        enable_lidar=True,
        enable_obd=True
    )
    for row in multimodal_iter:
        assert len(row) == 8
        timestamp, left_img, right_img, latitude, longitude, altitude, lidar, obd_dat = row
        assert type(timestamp) == float
        assert type(left_img) == np.ndarray
        assert left_img.dtype == np.uint8
        assert type(right_img) == np.ndarray
        assert right_img.dtype == np.uint8
        assert type(lidar) == np.ndarray
        assert type(obd_dat) == pd.DataFrame
        assert type(latitude) == np.float64
        assert type(longitude) == np.float64
        assert type(altitude) == np.float64
