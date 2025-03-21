init python:
    side_image_only_mode = False
    def callback_builder(character_sprite_basename):
        def char_callback(event, **kwargs):
            # Get the current attributes

            global side_image_only_mode

            if side_image_only_mode: return
            
            current_attributes = list(renpy.get_attributes(character_sprite_basename))
            print("Raw attributes:", current_attributes)  # Debugging output

            # Define allowed expressions
            valid_expressions = ["neutral", "happy", "worried", "thinking", "frustrated", "serious", "smile"]
            chosen_emotion = "neutral"  # Default emotion

            # Extract the dominant emotion (ignoring _closed/_opened)
            for attr in current_attributes:
                base_attr = attr.replace("_closed", "").replace("_opened", "").replace("_talk", "")
                if base_attr in valid_expressions:
                    chosen_emotion = base_attr
                    break  # Use the first valid expression

            # Determine talking or resting state
            if event == "show_done":
                sprite_variant = f"{character_sprite_basename} {chosen_emotion}_talk"
            elif event == "slow_done":
                sprite_variant = f"{character_sprite_basename} {chosen_emotion}_closed"
                renpy.restart_interaction()  # Ensure smooth transition
            else:
                sprite_variant = f"{character_sprite_basename} {chosen_emotion}_opened"

            # Ensure previous attributes are cleared before applying the new one
            renpy.show(character_sprite_basename, what=None)  # Remove stacking issues

            # Print debug info for tracking
            print("Filtered emotion:", chosen_emotion)  
            print(f"Final sprite: {sprite_variant}")

            # Show the correct sprite with talking animation
            renpy.show(sprite_variant, layer="master")

        return char_callback

init:
    define config.layers = [
        'background',  # Default layer for backgrounds
        'master',      # Default layer for characters and objects
        'transient',   # Default layer for temporary effects
        'screens',     # Default UI layer (DO NOT REMOVE)
        'overlay',     # Default overlay layer
        'mask_layer',  # Your custom layer for masks
        'character_layer'
    ]
