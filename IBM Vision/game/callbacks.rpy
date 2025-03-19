init python:
    def callback_builder(character_sprite_basename):
        def char_callback(event, **kwargs):
            # Get currently active attributes (emotions)
            current_attributes = renpy.get_attributes(character_sprite_basename)
            print("Raw attributes:", current_attributes)  # Debugging output

            # Extract only the base emotion (remove _closed and _talk)
            filtered_attributes = [
                attr.replace("_closed", "").replace("_talk", "")
                for attr in current_attributes
            ]

            # Ensure only unique emotions are kept
            filtered_attributes = list(set(filtered_attributes))

            # Default to "neutral" if no valid emotion is found
            current_emotion = filtered_attributes[0] if filtered_attributes else "neutral"

            print("Filtered emotion:", current_emotion)  # Debugging output

            # Update the sprite based on the event
            if event == "show_done":
                renpy.show(f"{character_sprite_basename} {current_emotion}_talk", layer="master")
            elif event == "slow_done":
                renpy.show(f"{character_sprite_basename} {current_emotion}_closed", layer="master")
                renpy.restart_interaction()  # Ensure image updates correctly
        return char_callback
