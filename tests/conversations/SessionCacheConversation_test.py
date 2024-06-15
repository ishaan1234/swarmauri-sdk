import pytest
from swarmauri.standard.messages.concrete import SystemMessage, AgentMessage, HumanMessage, FunctionMessage
from swarmauri.standard.conversations.concrete.SessionCacheConversation import SessionCacheConversation

@pytest.mark.unit
def test_1():
    def test_conversation_history(max_size):
        try:
            conv = SessionCacheConversation(system_message_content=SystemMessage(content='systest'), max_size=max_size)
            conv.add_message(HumanMessage(content='human'))
            conv.add_message(AgentMessage(content='agent'))
            conv.add_message(HumanMessage(content='human2'))
            conv.add_message(AgentMessage(content='agent2'))
            conv.add_message(HumanMessage(content='human3'))
            conv.add_message(AgentMessage(content='agent3'))
            conv.add_message(HumanMessage(content='human4'))
            conv.add_message(AgentMessage(content='agent4'))
            assert conv.history[0].content == 'systest'
            if max_size > 1:
                assert conv.history[1].role != 'human'
            if not max_size % 2 and max_size == 2:
                assert conv.history[1].content == 'human4'
                assert conv.history[2].content == 'agent4'
            if not max_size % 2 and max_size == 4:
                assert conv.history[1].content == 'human3'
                assert conv.history[2].content == 'agent3'
                assert conv.history[3].content == 'human4'
                assert conv.history[4].content == 'agent4'
            if not max_size % 2 and max_size == 6:
                assert conv.history[1].content == 'human2'
                assert conv.history[2].content == 'agent2'
                assert conv.history[3].content == 'human3'
                assert conv.history[4].content == 'agent3'
                assert conv.history[5].content == 'human4'
                assert conv.history[6].content == 'agent4'
        except Exception as e:
            assert str(e) == 'must be divisible by 2'
        print(max_size, 'max_size passed')

    for max_size in range(0, 7, 1):
        test_conversation_history(max_size)

@pytest.mark.unit
def test_2():
    def test_conversation_history(max_size):
            try:
                conv = SessionCacheConversation(system_message_content=SystemMessage(content='systest'), max_size=max_size)
                conv.add_message(HumanMessage(content='human'))
                conv.add_message(AgentMessage(content='agent'))
                conv.add_message(HumanMessage(content='human2'))
                conv.add_message(AgentMessage(content='agent2'))
                conv.add_message(HumanMessage(content='human3'))
                conv.add_message(AgentMessage(content='agent3'))
                 
                assert conv.history[0].content == 'systest'
                if max_size > 1:
                    assert conv.history[1].role != 'human'
                
                if not max_size % 2 and max_size == 2:
                    assert conv.history[1].content == 'human3'
                    
                if not max_size % 2 and max_size == 4:
                    assert conv.history[1].content == 'human2'
                    assert conv.history[2].content == 'agent2'
                    assert conv.history[3].content == 'human3'
                    assert conv.history[4].content == 'agent3'
                if max_size == 5:
                    assert conv.history[1].content == 'human2'
                    assert conv.history[2].content == 'agent2'
                    assert conv.history[3].content == 'human3'
                    assert conv.history[4].content == 'agent3'
                if not max_size % 2 and max_size == 6:
                    assert conv.history[1].content == 'human'
                    assert conv.history[2].content == 'agent'
                    assert conv.history[3].content == 'human2'
                    assert conv.history[4].content == 'agent2'
                    assert conv.history[5].content == 'human3'
                    assert conv.history[6].content == 'agent3'
            except Exception as e:
                assert str(e) == 'must be divisible by 2'
            print(max_size, 'max_size passed')

    for max_size in range(0, 7, 1):
        test_conversation_history(max_size)

@pytest.mark.unit
def test_3():
    def test_conversation_history(max_size):
        try:
            conv = SessionCacheConversation(system_message_content=SystemMessage(content='systest'), max_size=max_size)
            try:
                conv.add_message(AgentMessage(content='agent'))
            except Exception as e:     
                assert str(e) == "The first message in the history must be an HumanMessage."
        except Exception as e:
            assert str(e) == 'must be divisible by 2'
    for max_size in range(0, 7, 1):
        test_conversation_history(max_size)

@pytest.mark.unit
def test_4():
    def test_conversation_history(max_size):
        try:
            conv = SessionCacheConversation(system_message_content=SystemMessage(content='systest'), max_size=max_size)
            try:
                conv.add_message(HumanMessage(content='human'))
                conv.add_message(AgentMessage(content='agent'))
                conv.add_message(HumanMessage(content='human'))
                conv.add_message(HumanMessage(content='human'))
            except Exception as e:     
                print(str(e))
                assert str(e) == "Cannot have two repeating HumanMessages."
        except Exception as e:
            assert str(e) == 'must be divisible by 2'

            
        print(max_size, 'max_size passed test_conversation_eviction_4')
    for max_size in range(0, 7, 1):
        test_conversation_history(max_size)
