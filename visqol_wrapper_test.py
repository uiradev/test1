# In[1]
import visqol_wrapper as visqol


def test_guitar_48_stereo(duration, expected_mos_lqo):
    data_dir = visqol.VISQOL_DIR + "testdata/long_duration/1_min/"
    reference_file = data_dir + "guitar48_stereo_ref_" + duration + ".wav"
    degraded_file = data_dir + "guitar48_stereo_deg_" + duration + ".wav"

    mos_lqo = visqol.calculate(reference_file, degraded_file, timeout=120)
    print("MOS-LQO: {}".format(mos_lqo))
    assert mos_lqo == expected_mos_lqo, "MOS LQO {} does not match expect value {}".format(
        mos_lqo, expected_mos_lqo)


test_guitar_48_stereo("25s", 4.51776)
test_guitar_48_stereo("1min", 4.51121)

# %%
