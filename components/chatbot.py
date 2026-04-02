import reflex as rx
import os
from typing import Dict, List

class ChatState(rx.State):
    is_open: bool = False
    messages: List[Dict[str, str]] = [
        {"role": "assistant", "content": "Hi! 👋 Ready to help you shop!"}
    ]
    current_input: str = ""
    
    def toggle_chat(self):
        self.is_open = not self.is_open
    
    def send_message(self):
        if self.current_input.strip():
            self.messages.append({"role": "user", "content": self.current_input})
            self.current_input = ""
            
            api_key = os.getenv("GROQ_API_KEY")
            if api_key:
                # Simple non-blocking response for demo
                rx.set_timeout(self._mock_ai_response, 1000)
    
    def _mock_ai_response(self):
        self.messages.append({"role": "assistant", "content": "Great choice! Check our recommendations page. 🚀"})

def chatbot() -> rx.Component:
    """Floating AI chatbot - 100% Reflex compatible."""
    return rx.box(
        # Chat window
        rx.cond(
            ChatState.is_open,
            rx.card(
                rx.vstack(
                    # Header - FIXED spacing="3"
                    rx.hstack(
                        rx.icon(tag="bot"),
                        rx.heading("AI Assistant", size="5"),
                        rx.spacer(),
                        rx.button(rx.icon("x"), on_click=ChatState.toggle_chat),
                        width="100%",
                        spacing="2"
                    ),
                    
                    # Messages scroll - FIXED spacing="2"
                    rx.scroll_area(
                        rx.vstack(
                            rx.foreach(
                                ChatState.messages,
                                lambda m: rx.box(
                                    rx.text(m["content"]),
                                    bg=rx.cond(
                                        m["role"] == "user",
                                        "#3b82f6",
                                        "#e2e8f0"
                                    ),
                                    color=rx.cond(
                                        m["role"] == "user",
                                        "white",
                                        "#1e293b"
                                    ),
                                    padding="1rem",
                                    border_radius="lg",
                                    align_self=rx.cond(
                                        m["role"] == "user",
                                        "flex-end",
                                        "flex-start"
                                    ),
                                    max_width="85%"
                                )
                            ),
                            width="100%",
                            spacing="2"  # ✅ Reflex spacing scale
                        ),
                        height="300px",
                        width="100%"
                    ),
                    
                    # Input row - FIXED spacing="2"
                    rx.hstack(
                        rx.input(
                            placeholder="Ask about products...",
                            value=ChatState.current_input,
                            on_change=ChatState.set_current_input,
                            width="100%"
                        ),
                        rx.button("Send", on_click=ChatState.send_message),
                        spacing="2",  # ✅ Fixed
                        width="100%"
                    ),
                    
                    spacing="3",  # ✅ Fixed vstack spacing
                    width="100%"
                ),
                # Position fixed
                bottom="100px",
                right="20px",
                position="fixed",
                width="380px",
                z_index="9999"
            )
        ),
        
        # FAB button
        rx.button(
            rx.icon(tag="message_circle"),
            bottom="20px",
            right="20px",
            position="fixed",
            on_click=ChatState.toggle_chat,
            color_scheme="blue",
            size="4",
            border_radius="full"
        )
    )