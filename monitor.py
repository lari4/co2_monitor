from subprocess import Popen, PIPE


def send_data(type, data):
    pass


def main():
    import time
    time.sleep(60)
    print("Start CO2 monitor service")
    try:
        with Popen(["./co2mond"], stdout=PIPE) as process:
            for line in process.stdout:
                type, data = line.decode("utf-8").strip().split('\t')
                if type == 'CntR':
                    send_data('Co2', int(data))
                if type == 'Tamb':
                    send_data('Temp', float(data))
    except (KeyboardInterrupt, SystemExit):
        print("Stop service")


if __name__ == '__main__':
    main()