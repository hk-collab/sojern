#!/usr/bin/evn python3

def compare_versions(version1, version2):
    v1_labels = version1.split('.')
    v2_labels = version2.split('.')

    len_v1_labels = len(v1_labels)
    len_v2_labels = len(v2_labels)

    min_labels = len_v1_labels
    if len_v1_labels < len_v2_labels:
        v1_labels.append('0')
        min_labels = len_v1_labels + 1
    elif len_v2_labels < len_v1_labels:
        v2_labels.append('0')
        min_labels = len_v2_labels + 1

    for idx in range(min_labels):
        label1 = int(v1_labels[idx])
        label2 = int(v2_labels[idx])

        if label1 == label2:
            continue
        if label1 < label2:
            return -1
        return 1
    return 0


if __name__ == '__main__':
    print(compare_versions('1.0', '1.0'))
    print(compare_versions('2.0', '1.0'))
    print(compare_versions('1.9', '1.10'))
    print(compare_versions('1.9', '1.10.4'))
    print(compare_versions('1.9.4', '1.9'))
    print(compare_versions('2.1.4.3.4.2', '2.3'))
