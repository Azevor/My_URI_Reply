'''
Read an integer value, which is the duration in seconds of a certain event in a
factory, and inform it expressed in hours:minutes:seconds.
'''


class Time:

    def __init__(self, p_Seconds):
        self.m_Seconds = p_Seconds
        self.m_Format = []

    def convertToTime(self):
        v_Hour = int((self.m_Seconds/60)/60)

        if v_Hour > 0:
            self.m_Seconds -= v_Hour*60*60
        v_Minutes = int(self.m_Seconds/60)
        if v_Minutes > 0:
            self.m_Seconds -= v_Minutes*60

        # print('{}:{}:{}'.format(v_Hour, v_Minutes, self.m_Seconds))
        self.m_Format.append(v_Hour)
        self.m_Format.append(v_Minutes)
        self.m_Format.append(self.m_Seconds)

        return self.m_Format

    def __str__(self):
        return '{}:{}:{}'.format(self.m_Format[0], self.m_Format[1],
                                 self.m_Format[2])


if __name__ == '__main__':
    v_Time = Time(int(input()))

    v_Time.convertToTime()
    print(v_Time)
