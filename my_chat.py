import chainlit as cl
import my_chain


@cl.langchain_factory(use_async=True)
def factory():
    return my_chain.create_chain()
