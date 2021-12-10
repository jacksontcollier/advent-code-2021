#!/usr/bin/env python3

class SignalPattern(object):
    def __init__(self, segment_str):
        self.segment_str = ''.join(sorted(segment_str))
        self.segment_count = len(self.segment_str)
        self.segments = set(self.segment_str)

    def get_segment_count(self):
        return self.segment_count

    def get_segment_str(self):
        return self.segment_str

    def num_segments_common(self, signal_pattern):
        num_in_common= 0

        for segment in signal_pattern.get_segment_str():
            if segment in self.segments:
                num_in_common += 1

        return num_in_common

