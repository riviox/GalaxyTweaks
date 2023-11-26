import org.jetbrains.compose.desktop.application.dsl.TargetFormat
import org.jetbrains.kotlin.gradle.ExperimentalKotlinGradlePluginApi

plugins {
    kotlin("multiplatform")
    id("org.jetbrains.compose")
}

kotlin {
    jvm {
        @OptIn(ExperimentalKotlinGradlePluginApi::class)
        mainRun {
            mainClass = "MainKt"
        }
    }

    sourceSets {
        jvmMain {
            dependencies {
                implementation(compose.desktop.currentOs)
                implementation(project(":App:Common"))
            }
        }
    }
}

compose.desktop {
    application {
        mainClass = "MainKt"

        nativeDistributions {
            packageName = "Galaxy Tweaks"
            packageVersion = "4.0.0"
            targetFormats = setOf(TargetFormat.Exe, TargetFormat.Rpm, TargetFormat.Deb)

            windows {
                menu = true
                upgradeUuid = "b5fd1cad-350c-4e87-bf8f-4b309180c547"
            }
        }
    }
}