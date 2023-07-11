import threading
import time


class RepeatingFunction:
  """
    This is a class that takes a list of functions and spwns them as threads.
    See the test code as example of usage.
    """
  
  def __init__(self, func_list, interval=1):
    self.__pause = interval
    self._event = threading.Event()
    self._thread = threading.Thread(target=self._repeat_func,
                                    args=(func_list, ))
    self._running = False

  def start(self):
    if not self._running:
      self._running = True
      self._thread.start()

  def stop(self):
    if self._running:
      self._event.set()
      self._thread.join()
      self._running = False

  def _repeat_func(self, func, index=0):
    while not self._event.is_set():
      func[index]()
      self._event.wait(self.__pause)
      index = (index + 1) % len(func)


if __name__ == '__main__':

  def print_hello():
    print("Hello, world!")

  def print_bye():
    print("Bye, world!")

  repeating_function = RepeatingFunction([print_hello, print_bye])
  repeating_function.start()

  time.sleep(10)

  # Do other things here while the function repeats...

  repeating_function.stop()