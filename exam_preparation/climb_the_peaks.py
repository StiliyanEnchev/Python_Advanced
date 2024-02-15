from collections import deque

food = [int(x) for x in input().split(", ")]
stamina = deque([int(x) for x in input().split(", ")])

conquered_peaks = []
day = 0
all_conquered = False

peaks_dict = [
    ["Vihren", 80],
    ["Kutelo", 90],
    ["Banski Suhodol", 100],
    ["Polezhan", 60],
    ["Kamenitza", 70]
]

for day in range(7):
    current_food = food.pop()
    current_stamina = stamina.popleft()
    peak_to_climb, needed_sum = peaks_dict[0][0], peaks_dict[0][1]

    total_stamina_that_day = current_stamina + current_food

    if total_stamina_that_day >= needed_sum:
        conquered_peaks.append(peak_to_climb)
        peaks_dict.pop(0)

    if len(peaks_dict) == 0:
        all_conquered = True
        break

if all_conquered:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")

elif len(conquered_peaks) == 0:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    print(*conquered_peaks, sep="\n")
