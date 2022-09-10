
def test_idd_multimodal():
    from idd_iterator import idd_multimodal_iterator
    multimodal_iter = idd_multimodal_iterator.IDDMultimodalIterator(
        idd_multimodal_path="idd_multimodal_mini/"
    )
    for row in multimodal_iter:
        assert len(row) == 5
        timestamp, left_img, right_img, lidar, obd_dat = row
        pass