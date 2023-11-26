import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue

object AppManager {
    var path: List<String> by mutableStateOf(listOf())

    val availableActions = listOf(
        Action(
            emoji = "⚡",
            name = "main tweaks",
            description = "Applies the main tweaks."
        ),
        Action(
            emoji = "\uD83C\uDF10",
            name = "internet tweaks",
            description = "Applies the internet tweaks"
        ),Action(
            emoji = "\uD83D\uDEE0\uFE0F",
            name = "advanced tweaks",
            description = "Applies tweaks choosen by you"
        )

    )

    data class Action(
        val emoji: String,
        val name: String,
        val description: String
    )
}