import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

@Composable
fun actionWidget(action: AppManager.Action) {
    Card(
        modifier = Modifier
            .padding(10.dp)
            .height(150.dp)
            .clip(CardDefaults.shape)
            .clickable {  }
    ) {
        Column(
            modifier = Modifier.padding(10.dp),
            verticalArrangement = Arrangement.spacedBy(10.dp)
        ) {
            Row(
                horizontalArrangement = Arrangement.spacedBy(10.dp),
                verticalAlignment = Alignment.CenterVertically
            ) {
                Text(
                    text = action.emoji,
                    fontFamily = emojiFont,
                    fontWeight = FontWeight.ExtraBold,
                    fontSize = 20.sp
                )

                Text(
                    text = action.name,
                    fontWeight = FontWeight.Medium,
                    fontSize = 35.sp
                )
            }

            Box(
                modifier = Modifier.absolutePadding(
                    left = 20.dp
                )
            ) {
                Text(
                    text = action.description,
                    color = Color.LightGray
                )
            }
        }
    }
}