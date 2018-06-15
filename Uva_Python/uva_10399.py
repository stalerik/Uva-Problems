import math
import sys
#file = sys.stdin.read()
#lines = file.split("\n")

"""
def calculate_watches(k, m):
	m_sec = 0
	m_min = 0
	m_h = 1
	k_sec = 0
	k_min = 0
	k_h = 0

	while True:
		for i in range(2):
			for  j in range(1, 13):
				for l in range(60):
					for n in range(60):
						m_sec += 1
						k_sec += 1

						if m_sec > 59:
							m_min += 1
							m_sec = 0

						if m_min > 59:
							m_h += 1
							m_min = 0

						if m_h > 12:
							m_h = 1

						if k_sec > 59:
							k_min += 1
							k_sec = 0

						if k_min > 59:
							k_h += 1
							k_min = 0

						if k_h > 12:
							k_h = 1
		m_sec -= m
		k_sec -= k
		if m_sec < 0:
			m_min -= 1
		if k_sec < 0:
			k_min -= 1
		if m_min < 0:
			m_h -= 1
		if k_min < 0:
			k_h -= 1

		if m_sec == k_sec:
			if m_min == k_min:
				print(m_h, "+++", k_h)
				if m_h == k_h:
					print(m_h, ":", m_min, "+++", k_h, ":", k_min)
						
a = calculate_watches(0, 0)
print(a)
"""
sec_in_day = 43200
def calculate (k,m):
	k_clock = -k
	m_clock = -m
	day = 1
	kuk = 0
	while True:
		if k_clock == sec_in_day:
			k_clock = -k * day
			print(k_clock)
		if m_clock == sec_in_day:
			print(m_clock)
			m_clock = -m * day
		kuk += 1
		if kuk == sec_in_day:
			day += 1
			kuk = 0
		k_clock += 1
		m_clock += 1
		if k_clock == m_clock:
			print(k_clock, "+++", m_clock, "---", day)


calculate(1,2)
