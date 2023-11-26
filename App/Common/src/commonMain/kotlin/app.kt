import androidx.compose.animation.*
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.absolutePadding
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowBackIosNew
import androidx.compose.material.icons.filled.Close
import androidx.compose.material.icons.filled.SettingsBackupRestore
import androidx.compose.material3.*
import androidx.compose.material3.windowsizeclass.ExperimentalMaterial3WindowSizeClassApi
import androidx.compose.material3.windowsizeclass.WindowWidthSizeClass
import androidx.compose.material3.windowsizeclass.calculateWindowSizeClass
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.dp

@OptIn(ExperimentalMaterial3WindowSizeClassApi::class, ExperimentalMaterial3Api::class)
@Composable
fun app(
    exit: () -> Unit
) {
    val windowSizeClass = calculateWindowSizeClass()

    MaterialTheme(
        colorScheme = darkColorScheme()
    ) {
        Scaffold(
            modifier = Modifier
                .fillMaxSize()
                .clip(RoundedCornerShape(4)),
            topBar = {
                TopAppBar(
                    title = {
                        Text(
                            text = "Galaxy tweaks",
                            fontWeight = FontWeight.Medium,
                            softWrap = false
                        )
                    },
                    navigationIcon = {
                        Box(
                            modifier = Modifier
                                .padding(10.dp)
                                .clip(RoundedCornerShape(25))
                                .background(darkColorScheme().surfaceColorAtElevation(10.dp))
                                .clickable(AppManager.path.isNotEmpty()) {
                                    AppManager.path = AppManager.path.dropLast(1)
                                }
                        ) {
                            Icon(
                                imageVector = Icons.Filled.ArrowBackIosNew,
                                contentDescription = "Go back",
                                tint = if (AppManager.path.isNotEmpty()) LocalContentColor.current
                                else LocalContentColor.current.copy(
                                    alpha = 0.38f
                                ),
                                modifier = Modifier.padding(10.dp)
                            )
                        }
                    },
                    actions = {
                        AnimatedContent(
                            targetState = AppManager.path == listOf("main"),
                            transitionSpec = {
                                fadeIn() togetherWith fadeOut()
                            }
                        ) {
                            if (it) {
                                IconButton(
                                    onClick = {}
                                ) {
                                    Icon(
                                        imageVector = Icons.Filled.SettingsBackupRestore,
                                        contentDescription = null
                                    )
                                }
                            }
                        }

                        AnimatedContent(
                            targetState = windowSizeClass.widthSizeClass != WindowWidthSizeClass.Compact,
                            transitionSpec = {
                                fadeIn() togetherWith fadeOut()
                            }
                        ) {
                            if (it) {
                                IconButton(
                                    onClick = exit
                                ) {
                                    Icon(
                                        imageVector = Icons.Filled.Close,
                                        contentDescription = "exit the application"
                                    )
                                }
                            }
                        }
                    },
                    colors = TopAppBarDefaults.topAppBarColors(
                        containerColor = darkColorScheme().surfaceColorAtElevation(1.dp)
                    )
                )
            }
        ) {
            Box(
                modifier = Modifier
                    .fillMaxSize()
                    .absolutePadding(
                        top = it.calculateTopPadding()
                    )
            ) {
                AnimatedContent(
                    targetState = AppManager.path,
                    transitionSpec = {
                        if (targetState.size > initialState.size) {
                            slideIn { objSize -> IntOffset(objSize.width, 0) } + fadeIn() togetherWith
                                    slideOut { objSize -> IntOffset(-objSize.width, 0) } + fadeOut()
                        } else if (targetState.size < initialState.size) {
                            slideIn { objSize -> IntOffset(-objSize.width, 0) } + fadeIn() togetherWith
                                    slideOut { objSize -> IntOffset(objSize.width, 0) } + fadeOut()
                        } else fadeIn() togetherWith fadeOut()
                    }
                ) { targetPath ->
                    if (targetPath.isEmpty()) {
                        welcomeScreen()
                    } else if (targetPath == listOf("main")) {
                        tweaksMenu()
                    } else {
                        exampleScreen()
                    }
                }
            }
        }
    }
}