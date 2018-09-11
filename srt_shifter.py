import re
import sys

# time_stamp_delimiter_regex = r'[,:]'
# time_stamp_regex = time_stamp_delimiter_regex.join([r'\d+'] * 4)
#
# encodings = ('utf-8', 'cp1252', 'latin_1')


class SrtShifter():
    def __init__(self):

        self.HOURS_LENGTH = 2
        self.MINS_LENGTH = 2
        self.SECS_LENGTH = 2
        self.MSECS_LENGTH = 3

        self.time_stamp_delimiter_regex = r'[,:]'
        self.time_stamp_regex = self.time_stamp_delimiter_regex.join([r'\d+'] * 4)

        self.encodings = ('utf-8', 'cp1252', 'latin_1')

    def convert_shift_to_msecs(self, shift):
        """
        :param shift: float, amount to shift subtitles by in seconds
        :return: shift_msecs: float, amount to shift subtitles by in milliseconds
        """
        shift = float(shift)
        shift_msecs = int(shift*1000)
        return shift_msecs

    def convert_timestamp_to_msecs(self, timestamp):
        """
        Converts timestamp in HH:MM:SS,mmm string form to milliseconds
        :param timestamp: string
        :return: msecs: timestamp in milliseconds
        """
        hours, mins, secs, msecs = re.split(self.time_stamp_delimiter_regex, timestamp)
        hours, mins, secs, msecs = int(hours), int(mins), int(secs), int(msecs)

        mins += 60 * hours
        secs += 60 * mins
        msecs += 1000*secs

        return msecs

    def convert_msecs_to_timestamp(self, msecs):
        """
        Converts timestamp in millseconds to HH:MM:SS,mmm string form
        :param msecs
        :return: timestamp string
        """
        hours = msecs//(60*60*1000)
        msecs = msecs % (60*60*1000)

        mins = msecs//(60*1000)
        msecs = msecs % (60*1000)

        secs = msecs//1000
        msecs = msecs % 1000

        return self.format_into_timestamp(hours, mins, secs, msecs)

    def format_into_timestamp(self, hours, mins, secs, msecs):
        """
        Converts hours mins secs msecs ints into a timestamp in HH:MM:SS,mmm string form
        :param hours
        :param mins
        :param secs
        :param msecs
        :return: timestamp string
        """

        hours = str(hours)
        while len(hours) < self.HOURS_LENGTH:
            hours = '0' + hours

        mins = str(mins)
        while len(mins) < self.MINS_LENGTH:
            mins = '0' + mins

        secs = str(secs)
        while len(secs) < self.SECS_LENGTH:
            secs = '0' + secs

        msecs = str(msecs)
        while len(msecs) < self.MSECS_LENGTH:
            msecs = '0' + msecs

        return ":".join((hours, mins, secs)) + ',' + msecs

    def shift_timestamp(self, shift, timestamp):
        """
        Shift an individual timestamp by time (in seconds) specified by shift.
        :param shift: float, how much to shift timestamp by (in seconds)
        :param timestamp
        :return: shifted timestamp
        """

        shift_msecs = self.convert_shift_to_msecs(shift)
        timestamp_msecs = self.convert_timestamp_to_msecs(timestamp)
        shifted_timestamp_msecs = timestamp_msecs + shift_msecs
        new_timestamp = self.convert_msecs_to_timestamp(shifted_timestamp_msecs)

        return new_timestamp

    def create_shifted_srt_file(self, shift, srt_text, time_stamps, srt_file_path):
        new_srt_text = srt_text
        for old_time_stamp in time_stamps:
            new_time_stamp = self.shift_timestamp(shift, old_time_stamp)
            new_srt_text = new_srt_text.replace(old_time_stamp, new_time_stamp)

        new_file = open(srt_file_path.strip('.srt')+'resync'+'.srt', 'w')
        new_file.write(new_srt_text)
        new_file.close()


def main(arg_list):
    print(arg_list)
    shift = float(arg_list[1])
    srt_file_path = str(arg_list[0])

    for enc in encodings:
        try:
            with open(srt_file_path, "r", encoding=enc) as srt_file:
                print('Encoding = ', enc)
                srt_text = srt_file.read()
                time_stamps = re.findall(time_stamp_regex, srt_text)
                create_shifted_srt_file(shift, srt_text, time_stamps, srt_file_path)
            break
        except Exception:
            print(enc, 'did not work.')
            if enc == encodings[-1]:
                sys.exit(1)
            continue

if __name__ == '__main__':
    main(sys.argv[1:])
