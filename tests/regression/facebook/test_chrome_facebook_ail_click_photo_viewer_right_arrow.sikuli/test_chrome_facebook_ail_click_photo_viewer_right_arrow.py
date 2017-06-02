# if you are putting your test script folders under {git project folder}/tests/, it will work fine.
# otherwise, you either add it to system path before you run or hard coded it in here.

INPUT_LIB_PATH = sys.argv[1]
sys.path.append(INPUT_LIB_PATH)

import os
import common
import basecase
import facebook

import shutil
import browser
import time


class Case(basecase.SikuliInputLatencyCase):

    def run(self):
        # Disable Sikuli action and info log
        com = common.General()
        com.infolog_enable(0)

        chrome = browser.Chrome()
        fb = facebook.facebook()

        chrome.clickBar()
        chrome.enterLink(self.INPUT_TEST_TARGET)
        fb._wait(component=fb.FACEBOOK_COMMENT_ICONS, timeout=15)

        sample1_fp = os.path.join(self.INPUT_IMG_SAMPLE_DIR_PATH, self.INPUT_IMG_OUTPUT_SAMPLE_1_NAME)
        sleep(2)
        capture_width = int(self.INPUT_RECORD_WIDTH)
        capture_height = int(self.INPUT_RECORD_HEIGHT)

        # Set mouse move delay time to 0 for immediately action requirement
        Settings.MoveMouseDelay = 0
        loc, screenshot, t1 = fb._il_click('[log] Mouse Click - Button Up', fb.FACEBOOK_HOVER_COMMENT_ICONS,
                                           capture_width, capture_height)

        t2 = time.time()
        com.updateJson({'t1': t1, 't2': t2}, self.INPUT_TIMESTAMP_FILE_PATH)
        shutil.move(screenshot, sample1_fp.replace(os.path.splitext(sample1_fp)[1], '.png'))


case = Case(sys.argv)
case.run()
