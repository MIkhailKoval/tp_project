from abc import ABC, abstractmethod


class Context(ABC):
	_state = None
	
	def __init__(self, state: 'State') -> None:
		self.transition_to(state)
		
	def transition_to(self, state: 'State'):
		print(f"Context: Transition to {type(state).__name__}")
		self._state = state
		self._state.context = self

	def request1(self):
		self._state.handle1()

	def request2(self):
		self._state.handle2()


class State(ABC):

	@property
	def context(self):
		return self._context

	@context.setter
	def context(self, context: 'Context'):
		self._context = context

	@abstractmethod
	def handle1(self):
		pass

	@abstractmethod
	def handle2(self):
		pass

class Game(State):
	def handle1(self):
		print("Game handles request1.")
		print("Game wants to change the state of the context.")
		self.context.transition_to(Menu())

	def handle2(self):
		pass


class Menu(State):
	def handle1(self):
		pass

	def handle2(self):
		print("Menu handles request2.")
		print("Menu wants to change the state of the context.")
		self.context.transition_to(Game())


if __name__ == "__main__":

	context = Context(Game())
	context.request1()
	context.request2()