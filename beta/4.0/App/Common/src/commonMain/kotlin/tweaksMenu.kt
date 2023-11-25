import androidx.compose.animation.AnimatedContent
import androidx.compose.animation.slideIn
import androidx.compose.animation.slideOut
import androidx.compose.animation.togetherWith
import androidx.compose.foundation.ExperimentalFoundationApi
import androidx.compose.foundation.basicMarquee
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.grid.GridCells
import androidx.compose.foundation.lazy.grid.LazyVerticalGrid
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Button
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.dp

@OptIn(ExperimentalFoundationApi::class)
@Composable
fun tweaksMenu() {
    LazyColumn(
        verticalArrangement = Arrangement.spacedBy(10.dp),
        modifier = Modifier.fillMaxSize()
            .padding(10.dp)
    ) {
        item {
            LazyVerticalGrid(
                columns = GridCells.Adaptive(210.dp),
                userScrollEnabled = false,
                modifier = Modifier.heightIn(
                    min = 0.dp,
                    max = 99999.dp
                )
            ) {
                for (action in AppManager.availableActions) {
                    item {
                        actionWidget(action)
                    }
                }
            }
        }

        item {
            var isMoreMenuExpanded by rememberSaveable { mutableStateOf(false) }

            TextButton(
                onClick = {
                    isMoreMenuExpanded = !isMoreMenuExpanded
                },
                modifier = Modifier.absolutePadding(left = 15.dp)
            ) {
                Text(
                    text = "more...",
                    color = Color.Red,
                    fontWeight = FontWeight.Medium
                )
            }

            AnimatedContent(
                targetState = isMoreMenuExpanded,
                transitionSpec = {
                    if (targetState) {
                        slideIn { objSize -> IntOffset(0, -objSize.height) } togetherWith
                                slideOut { objSize -> IntOffset(0, objSize.height) }
                    } else {
                        slideIn { objSize -> IntOffset(0, objSize.height) } togetherWith
                                slideOut { objSize -> IntOffset(0, -objSize.height) }
                    }
                },
                modifier = Modifier.absolutePadding(left = 15.dp)
            ) {
                if (it) {
                    Surface(
                        modifier = Modifier
                            .clip(RoundedCornerShape(20)),
                        tonalElevation = 10.dp,
                        shadowElevation = 20.dp
                    ) {
                        Box(
                            modifier = Modifier
                                .padding(10.dp),
                            contentAlignment = Alignment.CenterStart
                        ) {
                            Row(
                                horizontalArrangement = Arrangement.spacedBy(10.dp)
                            ) {
                                Button(
                                    onClick = {}
                                ) {
                                    Row(
                                        horizontalArrangement = Arrangement.spacedBy(2.dp)
                                    ) {
                                        Text(
                                            text = "\uD83E\uDDF9",
                                            softWrap = false,
                                            fontFamily = emojiFont
                                        )

                                        Text(
                                            text = "Cleaner",
                                            softWrap = false
                                        )
                                    }
                                }

                                Button(
                                    onClick = {}
                                ) {
                                    Row(
                                        horizontalArrangement = Arrangement.spacedBy(2.dp),
                                        modifier = Modifier.basicMarquee(
                                            iterations = 999999999
                                        )
                                    ) {
                                        Text(
                                            text = "\uD83D\uDDD1\uFE0F",
                                            softWrap = false,
                                            fontFamily = emojiFont
                                        )

                                        Text(
                                            text = "remove applied tweaks",
                                            softWrap = false,
                                            overflow = TextOverflow.Ellipsis
                                        )
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}