import androidx.compose.foundation.layout.*
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

@Composable
fun welcomeScreen() {
    Box(
        modifier = Modifier.fillMaxSize(),
        contentAlignment = Alignment.Center
    ) {
        Column(
            verticalArrangement = Arrangement.spacedBy(10.dp),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Text(
                text = "GalaxyTweaks",
                fontSize = 25.sp,
                fontWeight = FontWeight.Medium
            )

            Text(
                text = "A simple app to boost your computer's performance",
                softWrap = true,
                textAlign = TextAlign.Center,
                modifier = Modifier.width(250.dp)
            )

            Button(
                onClick = {
                    AppManager.path += "main"
                }
            ) {
                Text("Start")
            }
        }
    }
}